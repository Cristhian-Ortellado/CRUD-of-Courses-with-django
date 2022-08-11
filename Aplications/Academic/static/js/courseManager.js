(function () {
    const btnDelete = document.querySelectorAll('.btn-delete');
    
    btnDelete.forEach(btn=>{
        btn.addEventListener('click',(e)=>{
            
            const confirmation = confirm('Are you sure that you want to delete this record?');
            if (!confirmation) {
               e.preventDefault(); 
            }
        })
    })    
})();

