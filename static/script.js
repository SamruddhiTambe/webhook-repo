function fetchEvents() {
    fetch("/events")
        .then(response => response.json())
        .then(data => {
            const eventList = document.getElementById("eventList");
            eventList.innerHTML = "";
            data.forEach(msg => {
                const li = document.createElement("li");
                li.textContent = msg;
                eventList.appendChild(li);
            });
        });
}

// Fetch every 15 seconds
fetchEvents();
setInterval(fetchEvents, 15000);
