import { useContext, useState, useRef, useEffect, } from 'react'
import PageWrapper from '../../../WelcomeScreen/PageWrapper'
import bg from '../../../assets/background-collage.png'
import thinking_image  from '../../../assets/black_man_thinking.webp'
import { ArrowRight, ArrowLeft, CornerDownLeft, CornerDownRight, House} from 'lucide-react'
import { useNavigate } from "react-router-dom";
import woodTapSound from '../../../assets/sound/woodTap.mp3'


function Lesson1(){

const woodTap = useRef(new Audio(woodTapSound))
const thinking = "..."

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
    console.log('i have played')    
}

 const Pit = ({beadCount}) => {
        return(
            <>
                 <div className="w-27 h-27 rounded-full bg-[#5c3317] shadow-inner flex flex-wrap items-center justify-center gap-1 p-4">
                    <div className='grid grid-cols gap-1 justify-items-center items-center'></div>                        
                    {Array.from( {length: beadCount }).map((_, index) =>(
                        <div key={index}
                        className='rounded-full bg-gradient-to-br from-grey-600 to-green-300 size-4'></div>

                    ))}
                </div>
            </>

        )
    }

    const steps = [{
        step: '1',
        text: "Welcome! I'm Agokansie, your Oware companion. Whether this is your very first game or you're looking to sharpen your skills, I'll guide you every step of the way. By the end of this tutorial, you'll understand the rules, know how to capture seeds, and be ready to play your first complete game. Let's begin!",
        voice: 'Foolish boy Siaw'

    },{
        step: '2',
        text: "Oware is one of the oldest and most popular traditional African board games. It belongs to the Mancala family of games and has been played for centuries across West Africa. Although the rules are simple, mastering Oware requires planning, strategy, and careful thinking.",
        voice: 'Foolish boy Siaw'

    },{
        step: '3',
        text: "The objective is simple: collect more seeds than your opponent. There are forty-eight seeds in total, so collecting twenty-five guarantees victory. If each player collects twenty-four seeds, the game ends in a draw.",
        voice: 'Foolish boy Siaw'

    } ]

    const [currentStep, setCurrentStep] = useState(0)
    const [nextLesson, setNextLesson] = useState(false)

    const previousStep = () => {
        setCurrentStep((previous) => previous === 0 ? previous :  previous - 1)
        console.log(steps[currentStep].step)

        
    }

    const nextStep = () => {
        setCurrentStep((previous) => previous === steps.length - 1 ? previous : previous + 1)
        console.log(steps[currentStep].step)
    }

    const Lesson2Continuation = () => {
        if(currentStep === steps.length - 1){
            setNextLesson(true)
        } else {
            setNextLesson(false)
        }
    }

    useEffect(() => {
        Lesson2Continuation()
    }, [currentStep])

    const Lesson2Navigation = () => {
        if (nextLesson){
            navigate('/lesson2')
        } 
        else{
            nextStep()
        }
    }


return(
<PageWrapper>
    <div className='absolute inset-0 bg-linear-to-r from-[#d4a017]/80 via-[#8b5a2b]/70 to-[#3b1f0f]/80 -z-1 min-h-screen flex flex-col items-center justify-center'>
        <img src={bg} alt="background image" className="absolute object-cover w-full h-full -z-1 opacity-[0.3]"/>   
    </div> 

    <div className='flex flex-col h-screen w-full'>

    <div className="absolute top-0 right-0 flex items-center gap-4 z-50 bg-dark/50 p-3 rounded-bl-lg">
        <ArrowLeft className=' left-3 size-8 cursor-pointer text-midGold' onClick={goBack} />
        <ArrowRight className=' size-8 text-gold-300 cursor-pointer text-midGold' onClick={goForward} />
        <House className=' size-7 text-gold-300 cursor-pointer text-midGold' onClick={() => {navigate('/selectionScreen')}}/>

    </div>


    <div className='flex flex-row items-start gap-4 p-6 shrink-0 ' >
        
            <img src={thinking_image} className='h-40 mt-15'/>

            <div>
                {/* <div>
                    <p className='text-4xl text-white'>
                        {
                            thinking.split("").map((dot, index) => (
                                <span
                                    key={index}
                                    style={{animationDelay: `${index * 0.2}s`}}
                                    className='inline-block animate-float'
                                >{dot}
                                </span>
                            ))
                        }
                    </p>
                </div> */}
                        
                <div className='relative w-[50%] shadow-lg rounded-lg p-3 text-[17px] backdrop-blur-md text-white bg-dark/30 mt-20 -ml-10'>
                    <p>{steps[currentStep].text}</p>
                </div>
                
            </div>          
        </div>

        <button onClick={Lesson2Navigation} className='absolute bottom-5 right-5 border-none p-3 text-xl rounded-lg cursor-pointer bg-gradient-to-br from-[#A47551] to-[#6B4226] text-[#F7E7CE] uppercase font-bold hover:scale-95 transition-smooth duration-300 flex items-center justify-center gap-3 bg-dark/30'> 
            <p>{nextLesson ? 'Next Lesson' : 'Next'}</p>
            <CornerDownRight /> 
        </button>

        <button onClick={previousStep} className='absolute bottom-5 left-5 border-none p-3 w-40 text-xl rounded-lg cursor-pointer bg-gradient-to-br from-[#A47551] to-[#6B4226] text-[#F7E7CE] uppercase font-bold hover:scale-95 transition-smooth duration-300 flex items-center justify-center gap-3'> 
            <CornerDownLeft /> 
            <p>Previous</p>
        </button>

    
        <div className='absolute left-1/2 -translate-x-1/2 border-2 border-t-0 border-midGold rounded-br-lg rounded-bl-lg px-6 py-2 text-center bg-dark/90 text-darkgold shadow-midgold shadow-sm'>

            <div>
                <p className='uppercase text-3xl font-bold font-fingerpaint'>Introdution to oware</p>
            </div>

            <div className='flex items-center justify-between'>
                <p className=' text-midGold'>Lesson 1</p>
                <p className='text-midGold'>{`Step ${steps[currentStep].step}`}</p>
            </div>
            
        </div>

        <div className="flex-1 flex items-center justify-center">

                <div className="flex flex-col items-center">

                    <div className="w-67 h-22 bg-[#6b3f1d] border-4 border-b-0 border-[#4a2a12] rounded-t-[3rem] shadow-2xl flex items-center justify-center gap-3 p-4">
                        <div className="w-65 h-17 bg-[#5c3317] rounded-t-[3rem] shadow-2xl flex items-center justify-center gap-3 p-4">
                        </div>
                    </div>

                    <div className="bg-[#8b5a2b] p-6 border-x-4 border-[#5a3418] shadow-2xl rounded-4xl">

                    <div className="flex gap-4 mb-5">

                        <Pit/>
                        <Pit/>
                        <Pit/>
                        <Pit/>
                        <Pit/>
                        <Pit/> 

                    </div>

                    <div className="flex gap-4">
                        <Pit/>
                        <Pit />
                        <Pit/>
                        <Pit />
                        <Pit />
                        <Pit/>

                    </div>

                    </div>

                    <div className="w-67 h-22 bg-[#6b3f1d] border-4 border-t-0 border-[#4a2a12] rounded-b-[3rem] shadow-2xl flex items-center justify-center gap-3 p-4">
                        <div className="w-65 h-17 bg-[#5c3317] rounded-b-[3rem] flex items-center justify-center gap-3 p-4">
                    </div>
                    </div>

            </div>

            </div>
        
        

        
    
    </div>
</PageWrapper>


)
}

export default Lesson1