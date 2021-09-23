const clearAll = document.getElementById('clear-filters')
clearAll.addEventListener("click",clearFilters)



function clearFilters(){
    document.getElementById("id_directors").value = ""
    document.getElementById("id_genre").value = ""
    document.getElementById("id_studio").value = ""
    
  }