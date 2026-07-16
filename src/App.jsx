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
import OwareLesson1 from './PlayGame/Tutorial/Lessons/owareLessons/Lesson1.jsx'
import OwareLesson2 from './PlayGame/Tutorial/Lessons/owareLessons/Lesson2.jsx'
import OwareLesson3 from './PlayGame/Tutorial/Lessons/owareLessons/Lesson3.jsx'
import OwareLesson4 from './PlayGame/Tutorial/Lessons/owareLessons/Lesson4.jsx'
import OwareLesson5 from './PlayGame/Tutorial/Lessons/owareLessons/Lesson5.jsx'
import OwareLesson6 from './PlayGame/Tutorial/Lessons/owareLessons/Lesson6.jsx'
import OwareLesson7 from './PlayGame/Tutorial/Lessons/owareLessons/Lesson7.jsx'



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
                <Route path='/owarelesson1' element={<OwareLesson1/>}/>
                <Route path='/owarelesson2' element={<OwareLesson2/>}/>
                <Route path='/owarelesson3' element={<OwareLesson3/>}/>
                <Route path='/owarelesson4' element={<OwareLesson4/>}/>
                <Route path='/owarelesson5' element={<OwareLesson5/>}/>
                <Route path='/owarelesson6' element={<OwareLesson6/>}/>
                <Route path='/owarelesson7' element={<OwareLesson7/>}/>
                
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