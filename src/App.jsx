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
import DameLessonScreen from './PlayGame/Tutorial/DameLessonScreen.jsx'
import AchiLessonScreen from './PlayGame/Tutorial/AchiLessonScreen.jsx'
import Lesson1 from './PlayGame/Tutorial/Lessons/owareLessons/Lesson1.jsx'
import Lesson2 from './PlayGame/Tutorial/Lessons/owareLessons/Lesson2.jsx'
import Lesson3 from './PlayGame/Tutorial/Lessons/owareLessons/Lesson3.jsx'
import Lesson4 from './PlayGame/Tutorial/Lessons/owareLessons/Lesson4.jsx'
import Lesson5 from './PlayGame/Tutorial/Lessons/owareLessons/Lesson5.jsx'
import Lesson6 from './PlayGame/Tutorial/Lessons/owareLessons/Lesson6.jsx'
import Lesson7 from './PlayGame/Tutorial/Lessons/owareLessons/Lesson7.jsx'



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
                <Route path='/dameLessonScreen' element={<DameLessonScreen/>}/>
                <Route path='/achiLessonScreen' element={<AchiLessonScreen/>}/>
                <Route path='/owarelesson1' element={<Lesson1/>}/>
                <Route path='/owarelesson2' element={<Lesson2/>}/>
                <Route path='/owarelesson3' element={<Lesson3/>}/>
                <Route path='/owarelesson4' element={<Lesson4/>}/>
                <Route path='/owarelesson5' element={<Lesson5/>}/>
                <Route path='/owarelesson6' element={<Lesson6/>}/>
                <Route path='/owarelesson7' element={<Lesson7/>}/>
                
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