<?php setCookie("css", $_GET["choice"], time() + 5184000);
header("Location: ".$_GET["currentPage"]); ?>