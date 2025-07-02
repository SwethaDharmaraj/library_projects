<?php
$host = "localhost";
$user = "root";
$pass = "Swetha@28"; // Use your MySQL root password if set
$db = "library";

$conn = new mysqli($host, $user, $pass, $db);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
?>
