function power(a, b = 2) {

    if (b == 2) {

        return a * a
    }

    let value = 1

    for (let i = 0; i < b; i++) {

        value *= a
    }

    return value;
}


let r1 = power(3)
console.log(r1);

let r2 = power(3, 3)
console.log(r2);

let r3 = power(3, 5)
console.log(r3);
