<?php
mb_internal_encoding("UTF-8");
mb_language("uni");

$to = "grggeo@grggeo.cz";
$subject = "Formulář GRGGEO.cz";
$encoded_subject = mb_encode_mimeheader($subject, "UTF-8", "B");

$message = "";
foreach ($_POST as $key => $value) {
    $message .= $key . ": " . $value . "\n";
}

// Přidání správných hlaviček pro UTF-8
$headers = "From: " . mb_encode_mimeheader($_POST["email"], "UTF-8", "B") . "\r\n";
$headers .= "Content-Type: text/plain; charset=UTF-8\r\n";
$headers .= "MIME-Version: 1.0\r\n";

mail($to, $encoded_subject, $message, $headers);
?>

<!DOCTYPE html>
<html lang="cs">
<head>
    <meta charset="UTF-8">
    <title>GRG GEO s.r.o.</title>
    <link rel="icon" type="image/x-icon" href="assets/img/GRG bíly.png" />
    <style>
        body {
            background-color: #f4f4f4;
            font-family: "Segoe UI", sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }

        .message-box {
            background-color: #ffffff;
            padding: 40px 60px;
            border-radius: 15px;
            box-shadow: 0 0 20px rgba(0,0,0,0.1);
            text-align: center;
        }

        .message-box h1 {
            color: #2ecc71;
            margin-bottom: 20px;
        }

        .message-box p {
            font-size: 18px;
            color: #333;
        }

        .message-box a {
            display: inline-block;
            margin-top: 25px;
            text-decoration: none;
            background-color: #2ecc71;
            color: white;
            padding: 12px 24px;
            border-radius: 8px;
            transition: background-color 0.3s ease;
        }

        .message-box a:hover {
            background-color: #27ae60;
        }
    </style>
</head>
<body>
    <div class="message-box">
        <h1>✅ Zpráva byla úspěšně odeslána.</h1>
        <p>Děkujeme za odeslání formuláře. Brzy se vám ozveme.</p>
        <a href="index.html">Zpět na hlavní stránku</a>
    </div>
</body>
</html>
