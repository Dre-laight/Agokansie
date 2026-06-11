import React from 'react'
import WelcomeScreen from './WelcomeScreen/Welcome.jsx'
import SelectionScreen from './WelcomeScreen/SelectionScreen.jsx'
import GameScreen from './PlayGame/startGame.jsx'

import {BrowserRouter, Routes, Route, useLocation} from 'react-router-dom'
import { AnimatePresence } from 'framer-motion'


function AnimatedRoutes(){
    const location = useLocation()

    return(
        <AnimatePresence mode='wait'>
            <Routes location={location} key={location.pathname}>
                <Route path='/' element={<WelcomeScreen/>}/>
                <Route path='/selectionScreen' element={<SelectionScreen/>}/>
                <Route path='/gameScreen' element={<GameScreen/>}/>
            </Routes>
        </AnimatePresence>

    )
    
}

function App(){
   
    return (

        <BrowserRouter>
          <AnimatedRoutes/>
        </BrowserRouter>    

    )
}

export default App