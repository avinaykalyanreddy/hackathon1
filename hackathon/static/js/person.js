function soiltypeChange() {
    const soiltype = document.querySelector('select[name="soiltype"]').value;
    let p1 = document.getElementById('p1');

    if (soiltype === 'red_soil') {
        p1.innerHTML = '<label style="font-size: x-large;font-weight: bolder;">Crop Type</label><select name="croptype" onchange="nutrients()"><option value="wheat">Wheat</option><option value="maize">Maize</option><option value="sugar cane">Sugar Cane</option><option value="other" selected>Other</option></select>';
    } else if (soiltype === 'black_soil') {
        p1.innerHTML = '<label style="font-size: x-large;font-weight: bolder;">Crop Type</label><select name="croptype" onchange="nutrients()"><option value="rice">Rice</option><option value="maize">Maize</option><option value="cotton">Cotton</option><option value="sugar cane">Sugar Cane</option><option value="other" selected>Other</option></select>';
    } else {
        p1.innerHTML = '<label style="font-size: x-large;font-weight: bolder;">Crop Type</label><select name="croptype" onchange="nutrients()"><option value="other" selected>Other</option></select>';
    }

}

function nutrients() {
    document.getElementById('p2').style.display = 'block';
    document.getElementById('submit').style.display = 'block';
}
