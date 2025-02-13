from django.shortcuts import render
from django.http import JsonResponse
import json
import datetime
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.core.files.images import ImageFile
import pickle
import numpy as np
import pandas
from sklearn.cluster import DBSCAN

with open('store/savedModel/rules.pkl', 'rb') as f:
        rules = pickle.load(f)


from .models import *


def cartData(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer)
        items = order.cartitem_set.all()
        cartItems = order.get_cart_items
        return {'cartItems': cartItems, 'order': order, 'items': items}


def store(request):
    cartItems = None
    products = Product.objects.all()
    recommended = []
    if request.user.is_authenticated:
        data = cartData(request)
        cartItems = data['cartItems']
        currentCustomer=Customer.objects.get(user=request.user)
        orderedProduct = OrderedProduct.objects.filter(customer=currentCustomer)
        rcl = []
        for pd in orderedProduct:
            rc = rules[rules['antecedents']==pd.product.name].consequents.unique()
            rcl = rcl + list(rc)
        arr = np.unique(np.array(rcl))
        for item in arr:
            recommended.append(Product.objects.get(name=item))

    produce = Product.objects.filter(category='produce')
    bakery = Product.objects.filter(category='bakery')
    breakfast = Product.objects.filter(category='breakfast')
    snacks = Product.objects.filter(category='snacks')
    dry_goods_pasta = Product.objects.filter(category='dry goods pasta')
    canned_goods = Product.objects.filter(category='canned goods')
    dairy_eggs = Product.objects.filter(category='dairy eggs')
    beverages = Product.objects.filter(category='beverages')
    pantry = Product.objects.filter(category='pantry')
    alcohol = Product.objects.filter(category='alcohol')
    babies = Product.objects.filter(category='babies')
    household = Product.objects.filter(category='household')
    bulk = Product.objects.filter(category='bulk')
    deli = Product.objects.filter(category='deli')
    frozen = Product.objects.filter(category='frozen')
    international = Product.objects.filter(category='international')
    meat_seafood = Product.objects.filter(category='meat seafood')
    personal_care = Product.objects.filter(category='personal care')
    pets = Product.objects.filter(category='pets')

    list1 = [produce,bakery,breakfast,snacks,dry_goods_pasta,canned_goods,dairy_eggs,beverages,pantry,alcohol,babies,household,bulk,deli,frozen,international,meat_seafood,personal_care,pets]
    category = ['Produce','Bakery','Breakfast','Snacks','Dry_goods_pasta','Canned_goods','Dairy_eggs','Beverages','Pantry','Alcohol','Babies','Household','Bulk','Deli','Frozen','International','Meat_seafood','Personal_care','Pets']
    zipedProduct = zip(list1,category)


    transactions = OrderedProduct.objects.all()
    cid = []
    customer = []
    product = []
    quantity = []
    for transaction in transactions:
        cid.append(transaction.customer.user.id)
        product.append(transaction.product.name)
        quantity.append(transaction.quantity)
    dic = {'cid':cid,'product':product,'quantity':quantity}
    transactiondata = pandas.DataFrame(dic)
    transactiondata = transactiondata.groupby(['cid','product'])['quantity'].sum().unstack().reset_index().fillna(0)
    
    dbscan = DBSCAN(eps=3, min_samples=2)
    clusters = dbscan.fit_predict(transactiondata.drop(['cid'],axis=1))

    transactiondata['Cluster'] = clusters
    cluster =[]
    for i in range(transactiondata.Cluster.max()+1):
        cluster.append(transactiondata[transactiondata.Cluster==i].cid.values)

    usercluster = []
    for users in cluster:
        if request.user.id in users:
            usercluster = users
    preferences = []
    for id in usercluster:
        if id != request.user.customer.id:
            customer = User.objects.get(id=id)
            op = OrderedProduct.objects.filter(customer=customer.id)
            preferences.append(op)

    crecommended = []
    for pr in preferences:
        for pd in pr:
            crecommended.append(pd.product)

    recommended = recommended+crecommended
    recommended = pandas.Series(recommended).drop_duplicates().tolist()
    if len(recommended)>3:
            recommended = recommended[:3]


    
    context = {'products': products, 'cartItems': cartItems, 'recommended':recommended, 'len':len(recommended), 'zipedProduct':zipedProduct}
        
    return render(request, 'store/store.html', context)


def cart(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items': items, 'order': order, 'cartItems': cartItems}

    return render(request, 'store/cart.html', context)


def checkout(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items': items, 'order': order, 'cartItems': cartItems}


    if request.method=='POST':

        customer = request.user.customer
        product = CartItem.objects.all()
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        zipcode = request.POST['zipcode']
        for pd in product:
            obj1 = OrderedProduct(customer=customer,product=pd.product,quantity=pd.quantity)
            obj1.save()
            obj2 = PurchaseInfo(customer=customer,address=address,city=city,state=state,zipcode=zipcode,product=obj1)
            obj2.save()
        CartItem.objects.all().delete()

    return render(request, 'store/checkout.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer)

    orderItem, created = CartItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)



def detail(request,id):
    products = Product.objects.all()
    cartItems = None
    if request.user.is_authenticated:
        data = cartData(request)
        cartItems = data['cartItems']
    product = None
    for pd in products:
        if pd.id==id:
            product=pd
    userrating = UserRating.objects.filter(product=product)
    return render(request, 'store/product_details.html',{'product':product,'cartItems':cartItems,'userrating':userrating})

def profile(request):
    userinfo = PurchaseInfo.objects.filter(customer=request.user.customer).first()
    purchases = PurchaseInfo.objects.filter(customer=request.user.customer)
    return render(request, 'store/profile.html',{'userinfo':userinfo, 'purchases':purchases})


def logout_view(request):
    logout(request)
    return redirect('/')

def login(request):

    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Credentials Invalid')
            return redirect('login')
        
    return render(request,'store/login.html')

def register(request):
    form = CreateUserForm()
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = User.objects.last()
            Customer.objects.create(user=user,name=user.username,email=user.email)
            
    context ={'form':form}
    return render(request,'store/register.html',context)

def loadproduct(request):
    with open('store/savedModel/product.pkl', 'rb') as f:
        pd = pickle.load(f)
        for items in pd.items():
            for item in items[1]:
                Product.objects.create(name=item,price='1000',category=items[0])
            
    return redirect('/')

def recommendedProduct(request):
    recommended = []
    if request.user.is_authenticated:
        data = cartData(request)
        cartItems = data['cartItems']
        currentCustomer=Customer.objects.get(user=request.user)
        orderedProduct = OrderedProduct.objects.filter(customer=currentCustomer)
        rcl = []
        for pd in orderedProduct:
            rc = rules[rules['antecedents']==pd.product.name].consequents.unique()
            rcl = rcl + list(rc)
        arr = np.unique(np.array(rcl))
        for item in arr:
            recommended.append(Product.objects.get(name=item))

    
    transactions = OrderedProduct.objects.all()
    cid = []
    customer = []
    product = []
    quantity = []
    for transaction in transactions:
        cid.append(transaction.customer.user.id)
        product.append(transaction.product.name)
        quantity.append(transaction.quantity)
    dic = {'cid':cid,'product':product,'quantity':quantity}
    transactiondata = pandas.DataFrame(dic)
    transactiondata = transactiondata.groupby(['cid','product'])['quantity'].sum().unstack().reset_index().fillna(0)
    
    dbscan = DBSCAN(eps=3, min_samples=2)
    clusters = dbscan.fit_predict(transactiondata.drop(['cid'],axis=1))

    transactiondata['Cluster'] = clusters
    cluster =[]
    for i in range(transactiondata.Cluster.max()+1):
        cluster.append(transactiondata[transactiondata.Cluster==i].cid.values)

    for users in cluster:
        if request.user.customer.id in users:
            usercluster = users
    preferences = []
    for id in usercluster:
        if id != request.user.customer.id:
            customer = User.objects.get(id=id)
            op = OrderedProduct.objects.filter(customer=customer.id)
            preferences.append(op)

    crecommended = []
    for pr in preferences:
        for pd in pr:
            crecommended.append(pd.product)

    recommended = recommended+crecommended
    recommended = pandas.Series(recommended).drop_duplicates().tolist()

        
    return render(request,'store/recommended.html',{'cartItems': cartItems, 'recommended':recommended, 'len':len(recommended)})

def produce(request):
    if request.user.is_authenticated:
        data = cartData(request)
        cartItems = data['cartItems']
    products = Product.objects.filter(category='produce')
    return render(request,'category/produce.html',{'products':products, 'cartItems':cartItems})

def createDataframe(request):
    transactions = OrderedProduct.objects.all()
    cid = []
    customer = []
    product = []
    quantity = []
    for transaction in transactions:
        cid.append(transaction.customer.user.id)
        customer.append(transaction.customer.name)
        product.append(transaction.product.name)
        quantity.append(transaction.quantity)
    dic = {'cid':cid,'customer':customer,'product':product,'quantity':quantity}
    transactiondata = pandas.DataFrame(dic)
    import pickle
    with open('store/savedModel/transactiondata.pkl', 'wb') as f:  
        pickle.dump(transactiondata, f) 
    f.close()
    return redirect('/')


