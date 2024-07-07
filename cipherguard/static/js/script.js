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
        if (data.error) {
            throw new Error(data.error);
        }
        const keyDisplay = algorithm === 'RSA' ? 'Private Key (keep this secret!)' : 'Symmetric Key';
        document.getElementById('result').innerHTML = `
            <p>Encrypted: ${data.encrypted}</p>
            <p>${keyDisplay}:</p>
            <textarea readonly style="width: 100%; height: 100px;">${data.key}</textarea>
        `;
    })
    .catch(error => {
        console.error('Encryption error:', error);
        document.getElementById('result').innerHTML = `
            <p>Error: ${error.message}</p>
        `;
    });
}

function decryptMessage() {
    const encrypted = document.getElementById('encrypted').value;
    const algorithm = document.getElementById('decryptAlgorithm').value;
    let key = document.getElementById('key').value;

    // Ensure the key includes the header and footer for RSA
    if (algorithm === 'RSA' && !key.includes('-----BEGIN')) {
        key = `-----BEGIN PRIVATE KEY-----\n${key}\n-----END PRIVATE KEY-----`;
    }

    fetch('/decrypt', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ encrypted, algorithm, key }),
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            throw new Error(data.error);
        }
        document.getElementById('decryptResult').innerHTML = `
            <p>Decrypted: ${data.decrypted}</p>
        `;
    })
    .catch(error => {
        console.error('Decryption error:', error);
        document.getElementById('decryptResult').innerHTML = `
            <p>Error: ${error.message}</p>
        `;
    });
}