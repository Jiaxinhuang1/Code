function Grade() {
   var Question3 = document.getElementsByName("Question3[]")
   var Question4 = document.getElementsByName("Question4[]")
   var checkedThree = false
   var checkedFour = false
   for (var i=0; i < Question3.length; i++){
      if (Question3[i].checked){
         checkedThree = true
         break
      }
   }
   for (var i=0; i < Question4.length; i++){
      if (Question4[i].checked){
         checkedFour = true
         break
      }
   }
   if (checkedThree && checkedFour){
      document.getElementById("GradeBtn").type = "submit"
   }
   else {
      alert("Please make sure to answer all questions")
   }
}