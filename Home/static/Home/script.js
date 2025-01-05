function sendToWhatsApp(event) {
    event.preventDefault();  // Prevent form from submitting normally

    // Get form data
    var name = document.getElementById('name').value;
    var email = document.getElementById('email').value;
    var message = document.getElementById('message').value;

    // Debugging: Check if values are captured correctly
    console.log("Name: " + name);
    console.log("Email: " + email);
    console.log("Message: " + message);

    // Ensure all fields have values
    if (!name || !email || !message) {
        alert("Please fill in all fields.");
        return;
    }

    // Format the message to send to WhatsApp
    var messageText = `*New Contact Message*\n\nName: ${name}\nEmail: ${email}\nMessage: ${message}`;

    // WhatsApp link format (replace '2349155775787' with your actual WhatsApp number)
    var whatsappLink = `https://wa.me/2349155775787?text=${encodeURIComponent(messageText)}`;

    // Debugging: Check the WhatsApp link before redirecting
    console.log("WhatsApp Link: " + whatsappLink);

    // Redirect to WhatsApp
    window.location.href = whatsappLink;
  }