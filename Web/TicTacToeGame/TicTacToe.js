var XPlayer = true
var XScore = 0
var OScore = 0
function Display(current){
	if (XPlayer) {
		XPlayer = false
		current.innerText = "X"
		current.disabled = true
	}
	else {
		XPlayer = true
		current.innerText = "O"
		current.disabled = true;
	}
	WinCheck()
}

// function that checks if any has won
function WinCheck(){
	// get all the rows id
	R1C1 = document.getElementById("11")
	R1C2 = document.getElementById("12")
	R1C3 = document.getElementById("13")
	R2C1 = document.getElementById("21")
	R2C2 = document.getElementById("22")
	R2C3 = document.getElementById("23")
	R3C1 = document.getElementById("31")
	R3C2 = document.getElementById("32")
	R3C3 = document.getElementById("33")
	if (((R1C1.innerText == "X") && (R1C2.innerText == "X") && (R1C3.innerText == "X"))
		|| ((R2C1.innerText == "X") && (R2C2.innerText == "X") && (R2C3.innerText == "X"))
		|| ((R3C1.innerText == "X") && (R3C2.innerText == "X") && (R3C3.innerText == "X"))
		|| ((R1C1.innerText == "X") && (R2C1.innerText == "X") && (R3C1.innerText == "X"))
		|| ((R1C2.innerText == "X") && (R2C2.innerText == "X") && (R3C2.innerText == "X"))
		|| ((R1C3.innerText == "X") && (R2C3.innerText == "X") && (R3C3.innerText == "X"))
		|| ((R1C1.innerText == "X") && (R2C2.innerText == "X") && (R3C3.innerText == "X"))
		|| ((R1C3.innerText == "X") && (R2C2.innerText == "X") && (R3C1.innerText == "X"))) {
		alert("X has won")
		XScore ++
		document.getElementById("XScore").innerHTML = XScore
		// disable all buttons when won
		document.querySelectorAll('button.slot').forEach(btn => {
			btn.disabled = true
		})
	}
	if (((R1C1.innerText == "O") && (R1C2.innerText == "O") && (R1C3.innerText == "O"))
		|| ((R2C1.innerText == "O") && (R2C2.innerText == "O") && (R2C3.innerText == "O"))
		|| ((R3C1.innerText == "O") && (R3C2.innerText == "O") && (R3C3.innerText == "O"))
		|| ((R1C1.innerText == "O") && (R2C1.innerText == "O") && (R3C1.innerText == "O"))
		|| ((R1C2.innerText == "O") && (R2C2.innerText == "O") && (R3C2.innerText == "O"))
		|| ((R1C3.innerText == "O") && (R2C3.innerText == "O") && (R3C3.innerText == "O"))
		|| ((R1C1.innerText == "O") && (R2C2.innerText == "O") && (R3C3.innerText == "O"))
		|| ((R1C3.innerText == "O") && (R2C2.innerText == "O") && (R3C1.innerText == "O"))) {
		alert("O has won")
		OScore ++
		document.getElementById("OScore").innerHTML = OScore
		document.querySelectorAll('button.slot').forEach(btn => {
			btn.disabled = true
		})
}
}

//function that starts a new game
function NewGame(){
	//enable all buttons and remove text
	document.querySelectorAll('button.slot').forEach(btn => {
		btn.disabled = false
		btn.innerText = ""
	})
	XPlayer = true
}