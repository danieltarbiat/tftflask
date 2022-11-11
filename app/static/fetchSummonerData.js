const summonerNameAndRegion = Document.querySelectorAll("input");

summonerNameAndRegion.addEventListener('submit', () => {
    summonerNameAndRegion.preventDefault();
    const data = Object.fromEntries(summonerNameAndRegion)
})

async function getSummonerData(searchQuery) {
    const response = await fetch('http://127.0.0.1:5000/', {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        const data = await response.text()
    }).then(res => res.json())
        .then(data => console.log(data))
}