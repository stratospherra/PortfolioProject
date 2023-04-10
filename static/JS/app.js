const iconClose = document.querySelector('.icon-close-2')
const wrapper = document.querySelector('.wrapper-2')

const iconClose2 = document.querySelector('.icon-close-3')
const wrapper2 = document.querySelector('.wrapper-3')

iconClose.addEventListener('click', ()=>{
        wrapper.style.display = "none"
    })

const popups = document.querySelector('.pop-ups')



    popups.addEventListener('click', ()=>{
        wrapper.style.display = "block"

    })


    iconClose2.addEventListener('click', ()=>{
        wrapper2.style.display = "none"
    })


    const popups2 = document.querySelector('.pop-ups-2')

    popups2.addEventListener('click', ()=>{
        wrapper2.style.display = "block"
    })
