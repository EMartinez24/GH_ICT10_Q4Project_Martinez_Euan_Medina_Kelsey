import pyscript

document = pyscript.window.document
Gallery = document.getElementById("gallery-container")

Gallery.innerHTML = """
<div class="col-md-3 col-sm-6">
    <div class="card h-100 border-0 shadow-sm">
        <img src="images/IMG_2784.jpg" class="card-img-top">
        <div class="card-body">
            <h5 class="card-title text-center fw-bold mb-1">Mini Mart</h5>
        </div>
    </div>
</div>

<div class="col-md-3 col-sm-6">
    <div class="card h-100 border-0 shadow-sm">
        <img src="images/DSCF0446.jpg" class="card-img-top">
        <div class="card-body">
            <h5 class="card-title text-center fw-bold mb-1">Intramurals</h5>
        </div>
    </div>
</div>

<div class="col-md-3 col-sm-6">
    <div class="card h-100 border-0 shadow-sm">
        <img src="images/675013828_3896165863851123_2378233852156665513_n.jpg" class="card-img-top">
        <div class="card-body">
            <h5 class="card-title text-center fw-bold mb-1">Christmas Party</h5>
        </div>
    </div>
</div>

<div class="col-md-3 col-sm-6">
    <div class="card h-100 border-0 shadow-sm">
        <img src="images/CAT Graduation.jpeg" class="card-img-top">
        <div class="card-body">
            <h5 class="card-title text-center fw-bold mb-1">CAT Graduation</h5>
        </div>
    </div>
</div>
"""
