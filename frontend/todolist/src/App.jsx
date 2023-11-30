import { useState } from 'react'
import './App.css'
import { Outlet } from 'react-router'
import NavBar from './components/NavBar'
import {api} from "./utilities"


function App() {
  // if(localStorage.getItem("userToken")) {
  //   api.defaults.headers.common["Authorization"] = `Token ${userToken}`
  //   console.log(`axios request authorization header set to: ${api.defaults.headers.common["Authorization"]}`)
  // }

  return (
    <>
      <h1>Get It Done Lists</h1>
      <NavBar/>
      <Outlet />
    </>
  )
}

export default App
