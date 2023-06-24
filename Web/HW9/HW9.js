var img_src = new Array("agra_fort.jpg", "ajanta_ellora.jpg", "akshardham_temple.jpg", "gateway_of_india.jpg", "hawa_mahal.jpg", "mehrangarh_fort.jpg", "mysore_palace.jpg", "qutub_minar.jpg", "sun_temple.jpg", "taj_mahal.jpg", "victoria_memorial.jpg")
var img_caption = new Array("Agra Fort", "Ajanta Ellora", "Akshardham Temple", "Gateway of India", "Hawa Mahal", "Mehrangarh Fort", "Mysore Palace", "Qutub Minar", "Sun Temple", "Taj Mahal", "Victoria Memorial")
var idx = 0
var startedSlides = false
var slides = null

function ChangeImage()
{
    document.getElementById("image").src = img_src[idx]
    document.getElementById("imageCaption").innerHTML = img_caption[idx]

    idx ++
    if (idx == img_src.length){
        idx = 0
    }
    if (!startedSlides)
    {
        StartSlides()
        startedSlides = true
    }
}

function StartSlides()
{
    slides = setInterval(ChangeImage, 3000)
}

function EndSlides()
{
    slides = clearInterval(slides)
}