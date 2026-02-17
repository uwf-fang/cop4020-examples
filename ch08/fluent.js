class EmailBuilder {
    constructor() {
        this.email = {};
    }

    from(address) {
        this.email.from = address;
        return this; // This allows the chain to continue
    }

    to(address) {
        this.email.to = address;
        return this;
    }

    setSubject(subject) {
        this.email.subject = subject;
        return this;
    }

    send() {
        console.log(`Sending: "${this.email.subject}" to ${this.email.to}`);
        // Usually, the final method does NOT return 'this'
    }
}

// Fluent Usage:
const myEmail = new EmailBuilder();

myEmail.from("me@test.com")
       .to("you@test.com")
       .setSubject("Hello!")
       .send();