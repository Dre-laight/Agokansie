import { useContext, useState, useRef, useEffect, } from 'react'
import PageWrapper from '../../WelcomeScreen/PageWrapper'
import bg from '../../assets/background-collage.png'
import thinking_image  from '../../assets/black_man_thinking.webp'
import { ArrowRight, ArrowLeft, CornerDownLeft, CornerDownRight} from 'lucide-react'
import { useNavigate } from "react-router-dom";
import woodTapSound from '../../assets/sound/woodTap.mp3'
import lesson1 from '../../assets/archiLesson1.png'
import lesson2 from '../../assets/archiLesson2.png'
import lesson3 from '../../assets/archiLesson3.png'
import lesson4 from '../../assets/archiLesson5.png'
import lesson5 from '../../assets/lesson8.png'
import lesson6 from '../../assets/archiLesson6.png'
import lesson7 from '../../assets/dameLesson7.png'
import lesson8 from '../../assets/lesson8.png'


function AchiLessonScreen(){

const woodTap = useRef(new Audio(woodTapSound))

const navigate = useNavigate()

const goBack = () => {
        navigate(-1)
        woodTap.current.currentTime = 0
        woodTap.current.play()
    }

const goForward = () => {
    navigate(1)
    woodTap.current.currentTime = 0
    woodTap.current.play()
}

const getBoardState = () => {
    console.log('I have played')
}


return(
<PageWrapper>
    <div className='absolute inset-0 bg-linear-to-r from-[#d4a017]/80 via-[#8b5a2b]/70 to-[#3b1f0f]/80 -z-1 min-h-screen flex flex-col items-center justify-center'>
        <img src={bg} alt="background image" className="absolute object-cover w-full h-full -z-1 opacity-[0.3]"/>   
    </div> 

    <div className='flex flex-col h-screen w-full'>

    <div className="absolute top-0 right-0 flex items-center gap-4 z-50 bg-dark p-3 rounded-bl-lg">
        <ArrowLeft className=' left-3 size-8 cursor-pointer text-midGold ' onClick={goBack} />
        <ArrowRight className=' size-8 text-gold-300 cursor-pointer text-midGold' onClick={goForward}/>
    </div>

    <div className='absolute top-0 left-0 bg-dark p-3 rounded-br-lg'>
        <p className='font-elite font-bold text-midGold text-3xl text-center'>Select A Lesson</p>
    </div>


    <div className='flex flex-col gap-10 items-center justify-center min-h-screen'>
        <div className='grid grid-cols-4 items-center gap-x-10 gap-y-10'>

            <div className=' flex flex-col items-center gap-3 justify-start h-80 w-60 rounded-lg border-1 border-darkgold bg-dark/50 shadow-darkgold shadow-sm'>
                <p className='border-2 border-t-0 border-midGold rounded-br-lg rounded-bl-lg p-2 text-darkgold '>Lesson 1</p>

                <div className='flex flex-col items-center justify-center p-3 gap-2'>   
                        <img src={lesson1} className='size-30 rounded-full' />
                    
                    <p className='uppercase text-[18px] font-bold text-center text-midGold h-13'>Introduction to Achi</p>
                    <button className='border-1 p-2 rounded-lg w-20 text-[18px] font-semibold text-gold' onClick={()=>{navigate('/achilesson1')}}>Begin</button>
                </div>
                
            </div>
            
            <div className=' flex flex-col items-center gap-3 justify-start h-80 w-60 rounded-lg border-1 border-darkgold bg-dark/50 shadow-darkgold shadow-sm'>
                <p className='border-2 border-t-0 border-midGold rounded-br-lg rounded-bl-lg p-2 text-darkgold'>Lesson 2</p>
                <div className='flex flex-col items-center justify-center p-3 gap-2'>
                    <img src={lesson2} className='size-30 rounded-full' />
                    <p className='uppercase text-[18px] font-bold text-center text-midGold h-13'>General rules</p>
                    <button className='border-1 p-2 rounded-lg w-20 text-[18px] font-semibold text-gold' onClick={() => {navigate('/achilesson2')}}>Begin</button>
                </div>

            </div>
            <div className=' flex flex-col items-center gap-3 justify-center h-80 w-60 rounded-lg border-1 border-darkgold bg-dark/50 shadow-darkgold shadow-sm'>
                <p className='border-2 border-t-0 border-midGold rounded-br-lg rounded-bl-lg p-2 text-darkgold'>Lesson 3</p>

                <div className='flex flex-col items-center justify-start p-3 gap-2'>
                    <img src={lesson3} className='size-30 rounded-full' />
                    <p className='uppercase text-[18px] font-bold text-center text-midGold h-13'>Dropping pieces</p>
                    <button className='border-1 p-2 rounded-lg w-20 text-[18px] font-semibold text-gold ' onClick={() => {navigate('/achilesson3')}}>Begin</button>
                </div>
                
            </div>
            <div className=' flex flex-col items-center gap-3 justify-start h-80 w-60 rounded-lg border-1 border-darkgold bg-dark/50 shadow-darkgold shadow-sm'>
                <p className='border-2 border-t-0 border-midGold rounded-br-lg rounded-bl-lg p-2 text-darkgold'>Lesson 4</p>

                <div className='flex flex-col items-center justify-center p-3 gap-2'>
                    <img src={lesson4} className='size-30 rounded-full' />
                    <p className='uppercase text-[18px] font-bold text-center text-midGold h-13'>Making moves</p>
                    <button className='border-1 p-2 rounded-lg w-20 text-[18px] font-semibold text-gold ' onClick={() => {navigate('/achilesson4')}}>Begin</button>
                </div>
                
            </div>

        </div>

        <div className='flex items-center justify-center'>
            <div className='grid items-center grid-cols-2 gap-10'>
             <div className=' flex flex-col items-center gap-3 justify-start h-80 w-60 rounded-lg border-1 border-darkgold bg-dark/50 shadow-darkgold shadow-sm'>
                <p className='border-2 border-t-0 border-midGold rounded-br-lg rounded-bl-lg p-2 text-darkgold '>Lesson 5</p>

                <div className='flex flex-col items-center justify-center p-3 gap-2'>
                    <img src={lesson5} className='size-30 rounded-full' />
                    <p className='uppercase text-[18px] font-bold text-center text-midGold h-13'>Game ends</p>
                    <button className='border-1 p-2 rounded-lg w-20 text-[18px] font-semibold text-gold ' onClick={() => {navigate('/achilesson5')}}>Begin</button>
                </div>
                
            </div>
            <div className=' flex flex-col items-center gap-3 justify-start h-80 w-60 rounded-lg border-1 border-darkgold bg-dark/50 shadow-darkgold shadow-sm'>
                <p className='border-2 border-t-0 border-midGold rounded-br-lg rounded-bl-lg p-2 text-darkgold'>Lesson 6</p>

                <div className='flex flex-col items-center justify-center p-3 gap-2'>
                    <img src={lesson6} className='size-30 rounded-full' />  
                    <p className='uppercase text-[18px] font-bold text-center text-midGold h-13'>Tips and strategies</p>
                    <button className='border-1 p-2 rounded-lg w-20 text-[18px] font-semibold text-gold' onClick={() => {navigate('/achilesson6')}}>Begin</button>
                </div>
                
            </div>
        </div>
    </div>
    </div>
    

    
    </div>
</PageWrapper>


)
}

export default AchiLessonScreen