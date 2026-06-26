import {useRef} from 'react'
import WelcomeScreen from './WelcomeScreen/Welcome.jsx'
import SelectionScreen from './WelcomeScreen/SelectionScreen.jsx'
import GameScreen from './PlayGame/startGame.jsx'
import DameGame from './PlayGame/DameScreen.jsx'
import AchiGame from './PlayGame/AchiGameScreen.jsx'
import BackgroundMusic from './assets/sound/bg.m4a'
import {BrowserRouter, Routes, Route, useLocation} from 'react-router-dom'
import { AnimatePresence } from 'framer-motion'


function AnimatedRoutes(){
    const location = useLocation()
    const audioRef = useRef(null)

    const startMusic = () => {
        audioRef.current.play()
        audioRef.current.volume = 0.15
    }

    return(
        <>
        <audio ref={audioRef} src={BackgroundMusic} loop/>
        <AnimatePresence mode='wait'>
            <Routes location={location} key={location.pathname}>
                <Route path='/' element={<WelcomeScreen music={startMusic}/>}/>
                <Route path='/selectionScreen' element={<SelectionScreen/>}/>
                <Route path='/gameScreen' element={<GameScreen/>}/>
                <Route path='/dameScreen' element={<DameGame/>}/>
                <Route path='/achiScreen' element={<AchiGame/>}/>

            </Routes>
        </AnimatePresence>
        </>
        

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