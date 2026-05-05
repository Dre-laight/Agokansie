import React from 'react'
import bg from '../assets/background.png'

function WelcomeScreen(){
    return(
        <div className='relative flex h-screen w-full items-center justify-center overflow-x-hidden'>
            <img 
                src={bg}
                alt='game background'
                className='absolute w-full h-full object-cover'
            />

            <div className='relative flex flex-col justify-center items-center'>
                <p className='capitalize font-elite text-gold font-bold text-7xl'>Discover Ghanaian <br/> game culture with  </p>
                <p className='uppercase text-darkgold text-7xl font-bold font-kablammo'>Agokansie</p >
                <p className='text-xl mt-5 mb-10 text-orange-100 tracking-widest'>Play. Learn. Preserve</p>
                <div className=' flex items-center justify-center'>
                    <button className='border-none p-3 w-60 text-xl text-d rounded-lg animate-bounce cursor-pointer bg-gradient-to-br from-[#A47551] to-[#6B4226] text-[#F7E7CE] uppercase font-bold hover:w-50 transition-smooth duration-300'>Play Now</button>
                </div>
            </div>
            div
        </div>
    )
}

export default WelcomeScreen   