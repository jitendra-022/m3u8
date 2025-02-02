<?php
// URL passed as a query string parameter
$target_url = isset($_GET['url']) ? $_GET['url'] : null;

if ($target_url) {
    // Call the Python scraper script to get the HLS link
    $output = shell_exec("python3 scraper.py '$target_url'");
    
    // If a valid HLS link is found, redirect to it
    if ($output) {
        header("Location: $output");
        exit;
    } else {
        echo "No HLS link found!";
    }
} else {
    echo "Please provide a valid URL.";
}
?>
