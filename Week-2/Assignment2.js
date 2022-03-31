const btnClick = document.querySelector('.btn-main');
btnClick.addEventListener('click',() =>{
	const headline = document.getElementById('headline');
	headline.textContent = 'Have a Good Time!';
});

const btnToggle = document.querySelector('.btn-toggle');
btnToggle.addEventListener('click',()=>{
    const pageContainer = document.querySelector('.page2');
    if(pageContainer.style.display==='none'){
        pageContainer.style.display = 'block';
    }else{
        pageContainer.style.display = 'none';
    }
    
    
});