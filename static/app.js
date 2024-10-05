const BASE_URL = "http://127.0.0.1:5000/api"

let cupcakesList = $("#cupcakes-list")

function generateHTML(cupcake){
    return `
    <div data-cupcake-id=${cupcake.id}>
        <img src="${cupcake.image} alt="${cupcake.flavor} cupcake!">
            <li> Flavor: ${cupcake.flavor} | Size: ${cupcake.size} | Rating: ${cupcake.rating} | <button class="delete-button"><b>X</b></button>
            </li>
    </div>
    `;
}

async function getAllCupcakes(){
    try {
        const res = await axios.get(`${BASE_URL}/cupcakes`);
        for (let cupcake of res.data.cupcakes){
            let newCupcake = generateHTML(cupcake);
            cupcakesList.append(newCupcake);
        }
    } catch (error) {
        console.error("Error adding cupcake:", error.response.data);
        alert("Failed to add cupcake: " + error.response.data.error);
    }
}


$("#new-cupcake-form").on("submit", async function (e) {
    e.preventDefault();
  
    let flavor = $("#form-flavor").val();
    let rating = $("#form-rating").val();
    let size = $("#form-size").val();
    let image = $("#form-image").val();
  
    try {
        const res = await axios.post(`${BASE_URL}/cupcakes`, {
        flavor,
        rating,
        size,
        image
        });
    } catch (error) {
        console.error("Error adding cupcake:", error.response.data);
        alert("Failed to add cupcake: " + error.response.data.error);
    }
  
    let newCupcake = $(generateHTML(res.data.cupcake));
    $("#cupcakes-list").append(newCupcake);
    $("#new-cupcake-form").trigger("reset");
  });
  
  
 
  
  $("#cupcakes-list").on("click", ".delete-button", async function (e) {
    e.preventDefault();
    let $cupcake = $(e.target).closest("div");
    let cupcakeId = $cupcake.attr("data-cupcake-id");
    
    try{
        await axios.delete(`${BASE_URL}/cupcakes/${cupcakeId}`);
        $cupcake.remove(); 
        
    } catch (error) {
        console.error("Error adding cupcake:", error.response.data);
        alert("Failed to add cupcake: " + error.response.data.error);
        }
    }
); 
   


getAllCupcakes()
