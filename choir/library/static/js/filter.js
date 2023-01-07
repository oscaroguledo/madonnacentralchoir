const id_list = document.querySelectorAll('*[id]')
     for (d in id_list) {
          try {
                // for dates and days
              if (id_list[d].id.includes('date') || id_list[d].id.includes('day')){
                    const identity = id_list[d].id
                    //console.log(id_list[d].id, identity);
                   document.getElementById(identity).addEventListener("focus",(e)=>{
                    document.getElementById(identity).type = 'date';
                    //console.log(document.getElementById(identity).type);
                    })
              }
              //for passwords
              if (id_list[d].id.includes('password') || id_list[d].id.includes('pwd')){
                    const identity = id_list[d].id
                    //console.log(id_list[d].id, identity);
                   document.getElementById(identity).classList.replace('is-valid','is-invalid');

              }
               // for campuses
              if (id_list[d].id.includes('id_campus') || id_list[d].id.includes('campus')){
                    const identity = id_list[d].id
                    //console.log(id_list[d].id, identity);
                    document.getElementById(identity).addEventListener("change",(e)=>{

                    var option=e.options[e.selectedIndex].text;
                    console.log(option);
                    })

              }
          }
          catch(err) {
                console.log(err);
          }
        }