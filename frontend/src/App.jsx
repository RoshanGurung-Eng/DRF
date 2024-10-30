import React from 'react'
import {Route, Routes} from 'react-router-dom'
import HomePage from './pages/UserFrontend/HomePge'
import FrontendMain from './pages/UserFrontend/FrontendMain'
import AllCategory from './pages/UserFrontend/AllCategory'
import AllProducts from './pages/UserFrontend/AllProduct'
import AllCategoryProduct from './pages/UserFrontend/AllCategoryProduct'
import SingleProduct from './pages/UserFrontend/SingleProduct'
import CartPage from './pages/UserFrontend/CartPage'
import ContactPage from './pages/UserFrontend/ContactPage'
import LoginPage from './pages/Auth/LoginPage'
import RegisterPage from './pages/Auth/RegisterPage'
const App = () => {
  return (
    <Routes>
        <Route path='/' element={<FrontendMain />}>
            <Route index element={<HomePage />} />
            <Route path='category' element={<AllCategory />} />
            <Route path='product' element={<AllProducts />} />
            <Route path='singlecategory/:id' element={<AllCategoryProduct />} />
            <Route path='singleProduct/:id' element={<SingleProduct />} />
            <Route path='cart' element={<CartPage />} />
            <Route path='contact' element={<ContactPage />} />

            {/* Auth */}
            <Route path='login' element={<LoginPage />} />
            <Route path='register' element={<RegisterPage />} />
        </Route>
    </Routes>
  )
}

export default App