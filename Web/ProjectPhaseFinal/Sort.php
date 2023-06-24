<?php setCookie("Sort", $_GET["sort"], time() + 5184000);
header("Location: ".$_GET["currentPage"]); ?>