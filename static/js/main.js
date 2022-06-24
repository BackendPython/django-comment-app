let container = document.querySelector('.container-fuild')
let display = document.querySelector('.full2')
let loading = document.querySelector('.load')

window.addEventListener('beforeunload', function(){
    loading.style.display = 'flex'
    display.style.display = 'none'
    setTimeout(() => {
        loading.style.display = 'none'
        display.style.display = 'block'
    }, 3000);
})