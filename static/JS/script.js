const wrapper = document.querySelector('.wrapper')
const loginLink = document.querySelector('.login-link')
const registerLink = document.querySelector('.register-link')
const btnPopUp = document.querySelector('.btnLogin-popup')
const iconClose = document.querySelector('.icon-close')


// iconClose2.addEventListener('click', ()=>{
//   wrapper.classList.remove('')
//   // console.log('click')
// })

iconClose.addEventListener('click', ()=>{
    wrapper.classList.remove('active-popup')
})

registerLink.addEventListener('click', ()=>{
    wrapper.classList.add('active')
})

loginLink.addEventListener('click', ()=>{
    wrapper.classList.remove('active')
})


btnPopUp.addEventListener('click', ()=>{
    wrapper.classList.add('active-popup')
})

const arrow = document.querySelector('.arrow');

window.addEventListener('scroll', () => {
  if (window.scrollY > 100) {
    arrow.classList.add('hidden');
  } else {
    arrow.classList.remove('hidden');
  }
});



