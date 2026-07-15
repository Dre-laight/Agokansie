import {useRef} from 'react'
import WelcomeScreen from './WelcomeScreen/Welcome.jsx'
import SelectionScreen from './WelcomeScreen/SelectionScreen.jsx'
import OwareGame from './PlayGame/startGame.jsx'
import DameGame from './PlayGame/DameScreen.jsx'
import AchiGame from './PlayGame/AchiGameScreen.jsx'
import BackgroundMusic from './assets/sound/bg.m4a'
import {BrowserRouter, Routes, Route, useLocation} from 'react-router-dom'
import { AnimatePresence } from 'framer-motion'
import OwareLesson from './PlayGame/Tutorial/OwareLessonScreen.jsx'
import DameTutorial from './PlayGame/Tutorial/DameTutorial.jsx'
import AchiTutorial from './PlayGame/Tutorial/AchiTutorial.jsx'
import Lesson1 from './PlayGame/Tutorial/Lessons/Lesson1.jsx'
import Lesson2 from './PlayGame/Tutorial/Lessons/Lesson2.jsx'
import Lesson3 from './PlayGame/Tutorial/Lessons/Lesson3.jsx'
import Lesson4 from './PlayGame/Tutorial/Lessons/Lesson4.jsx'
import Lesson5 from './PlayGame/Tutorial/Lessons/Lesson5.jsx'
import Lesson6 from './PlayGame/Tutorial/Lessons/Lesson6.jsx'
import Lesson7 from './PlayGame/Tutorial/Lessons/Lesson7.jsx'

function AnimatedRoutes(){
    const location = useLocation()
    const audioRef = useRef(null)

    const startMusic = () => {
        audioRef.current.play()
        audioRef.current.volume = 0.05
    }

    return(
        <>
        <audio ref={audioRef} src={BackgroundMusic} loop/>  
        <AnimatePresence mode='wait'>
            <Routes location={location} key={location.pathname}>
                <Route path='/' element={<WelcomeScreen music={startMusic}/>}/>
                <Route path='/selectionScreen' element={<SelectionScreen/>}/>
                <Route path='/owareScreen' element={<OwareGame/>}/>
                <Route path='/dameScreen' element={<DameGame/>}/>
                <Route path='/achiScreen' element={<AchiGame/>}/>
                <Route path='/owareLessonScreen' element={<OwareLesson/>}/>
                <Route path='/dameTutorial' element={<DameTutorial/>}/>
                <Route path='/AchiTutorial' element={<AchiTutorial/>}/>
                <Route path='/lesson1' element={<Lesson1/>}/>
                <Route path='/lesson2' element={<Lesson2/>}/>
                <Route path='/lesson3' element={<Lesson3/>}/>
                <Route path='/lesson4' element={<Lesson4/>}/>
                <Route path='/lesson5' element={<Lesson5/>}/>
                <Route path='/lesson6' element={<Lesson6/>}/>
                <Route path='/lesson7' element={<Lesson7/>}/>
                


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