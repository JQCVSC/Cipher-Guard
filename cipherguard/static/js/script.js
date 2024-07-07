function encryptMessage() {
    const message = document.getElementById('message').value;
    const algorithm = document.getElementById('algorithm').value;

    fetch('/encrypt', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message, algorithm }),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerHTML = `
            <p>Encrypted: ${data.encrypted}</p>
            <p>Key: ${algorithm === 'RSA' ? 'Private Key (keep this secret!)' : data.key}</p>
            <textarea readonly>${data.key}</textarea>
        `;
    });
}

function decryptMessage() {
    const encrypted = document.getElementById('encrypted').value;
    const algorithm = document.getElementById('decryptAlgorithm').value;
    const key = document.getElementById('key').value;

    fetch('/decrypt', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ encrypted, algorithm, key }),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('decryptResult').innerHTML = `
            <p>Decrypted: ${data.decrypted}</p>
        `;
    });
}