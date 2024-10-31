import React from 'react'
import { HeaderComponent } from '../../components/Frontend/HeaderComponent'
import { Outlet } from 'react-router-dom'

const FrontendMain = () => {
  return (
    <div>
      <HeaderComponent/>
      <Outlet/>
    </div>
  )
}

export default FrontendMain