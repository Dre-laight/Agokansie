import React from 'react'
import WelcomeScreen from './WelcomeScreen/Welcome.jsx'
import SelectionScreen from './WelcomeScreen/SelectionScreen.jsx'
import GameScreen from './PlayGame/startGame.jsx'
import DameScreen from './PlayGame/DameScreen.jsx'
import AchiScreen from './PlayGame/AchiGameScreen.jsx'

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
                <Route path='/dameScreen' element={<DameScreen/>}/>
                <Route path='/achiScreen' element={<AchiScreen/>}/>

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