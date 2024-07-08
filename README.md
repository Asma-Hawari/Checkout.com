<p align="center">
<a href="https://www.checkout.com.com/en/"><img src="https://cdn.prod.website-files.com/64db80a5e88c6b1723ff760b/64e79842e86ad09a621d5417_logotype-lockup.svg" alt="Checkout.com"></a>
</p>

<p align="center"><a href="https://vuejs.org/" target="_blank"><img src="https://miro.medium.com/v2/resize:fit:1400/format:webp/1*0Rk_6tH6IeSu8RjGEMRxYg.png" width="400"></a></p>

## The Code Challenge

### The Main Task
In this section, you have to build a checkout page. You will find below a description of the requirements. Based on the requirements, and with the help of our documentation, you should determine the integration method to be used as well as which payment methods to provide. You should then code a minimalistic checkout page with all the necessary functionalities and features.

## The Solution

### The FrameWork

#### Django
is a free and open-source, Python-based web framework that runs on a web server. It follows the model–template–views architectural pattern.
#### Vue.js
is a  Progressive JavaScript Framework which will be here the Frontend for the application


Django with Vue.js is very powerful, very easy to use and provides tools required for large, robust applications.

### The Packages 

- Axios for APIs requests
- Bulma for rendering the webpages
- Djnago RestFul APIs

### The Database
- Sqlite3

## How to run the application?
ps:: The application has two servers one for the backend and one for Frontend and we will run them both 
1- Django
- download the repo on your local machine
- cd to the djackets_django 
- run the server " python manage.py runserver"

2- Vue.js
- download the repo on your local machine
- cd to the djackets_vue
- install npm modules
- run the server "npm run serve"



### About the Project

#### Home Page 
<p align="center">
<img src="Images/home" alt="get_user_data">
</p>


#### Product Page
the data will be imported from the CSV files once the command "seed" is run
  
#### 
PHPUnit Test is used to run tests for each endpoint , Negative and Positive tests are added


## Different Cases
<b>Register</b>

All the different Cases of Registration has been processed

<b>Creating new User</b>

<p align="center">
<img src="database/data/screenshots/register.png" alt="Register">
</p>

<b>Handing Validation Error</b>

<p align="center">
<img src="database/data/screenshots/validation-Register.png" alt="validation-Register">
</p>

<b>Handing Duplicate Entry Error</b>

<p align="center">
<img src="database/data/screenshots/duplicateEntry-register.png" alt="Duplicate Entry">
</p>

<b>Authentication</b>

All the different Cases of Authentication has been processed

<p align="center">
<img src="database/data/screenshots/auth.png" alt="Authentication">
</p>

<b>Get Products</b>

Get All The products - No Authentication Required

<p align="center">
<img src="database/data/screenshots/getallproducts.png" alt="get_all_products">
</p>

<b>Get User Data</b>

Get User name - Authentication Required

<p align="center">
<img src="database/data/screenshots/getUserData.png" alt="get_user_data">
</p>

<p align="center">
<img src="database/data/screenshots/getUserDataUnauthorized.png" alt="get_user_data">
</p>

<b>Get User's Purchased Items</b>

SKUs for all the purchased products - Authentication Required

<p align="center">
<img src="database/data/screenshots/getUserProducts.png" alt="get_user_products">
</p>

<b>Add Purchased Item to the user's purchased list</b>

SKU must be valid - Authentication Required

<p align="center">
<img src="database/data/screenshots/additemnotfound.png" alt="add_user_products">
</p>
<p align="center">
<img src="database/data/screenshots/addpurchasedItem.png" alt="add_user_products">
</p>

<b>Delete Purchased Item from the user's purchased list</b>

SKU must be valid - Authentication Required

<p align="center">
<img src="database/data/screenshots/deletenotfound.png" alt="delete_user_product">
</p>
<p align="center">
<img src="database/data/screenshots/DeletePurchasedItem.png" alt="delete_user_product">
</p>

## suggested improvements
- Integrates with CI/CD processes on GitLab.
- make more tests to catch every exception that might be thrown.
- Add Tests For Database actions.
 
## License
The Django framework is open-sourced software licensed under the [MIT license](https://opensource.org/licenses/MIT).
