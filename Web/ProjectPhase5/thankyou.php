

<?php
if(isset($_POST['submitform']))
{
    $name = $_POST["name"];

$nameString = strval($name);

}
echo "<a href='Homepage.php'>Back to Home</a>";
?>
<script>
    var nameString = '<?=$nameString?>';
    alert("Thank you, " + nameString + ". Your response has been recorded.");
</script>
