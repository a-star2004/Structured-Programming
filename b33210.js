/**
 * Name: Esther Athieno
 * Access Number: B33210
 * Registration Number: M25B13/003
 
 * 
 * Problem: School Fee Payment System
 * This program helps a school track students’ fee payments, calculate balances and determine whether a student has cleared or not.
 */

// Function to calculate balance
function calculateBalance(totalFee, amountPaid) {
    return totalFee - amountPaid;
}

// Function to check payment status using conditions
function checkStatus(balance) {
    if (balance === 0) {
        return "Fully Paid";
    } else if (balance > 0 && balance <= 100000) {
        return "Almost Cleared (Balance Small)";
    } else if (balance > 100000) {
        return "Not Cleared";
    } else {
        return "Overpaid (Extra money paid)";
    }
}

// Function to display fee report for multiple students
function displayReport(students) {
    console.log("=== SCHOOL FEE PAYMENT REPORT ===");

    // Loop through each student
    for (let i = 0; i < students.length; i++) {
        let student = students[i];

        let balance = calculateBalance(student.totalFee, student.amountPaid);
        let status = checkStatus(balance);

        console.log("\nStudent Name: " + student.name);
        console.log("Class: " + student.className);
        console.log("Total Fee: " + student.totalFee);
        console.log("Amount Paid: " + student.amountPaid);
        console.log("Balance: " + balance);
        console.log("Status: " + status);
    }
}

// Example student data
let studentList = [
    { name: "Kyazze Vincent", className: "Senior One", totalFee: 500000, amountPaid: 500000 },
    { name: "Martha Lunyolo", className: "Senior Two", totalFee: 600000, amountPaid: 480000 },
    { name: "Atule Michael", className: "Senior Three", totalFee: 550000, amountPaid: 400000 },
    { name: "Princess Jera", className: "Senior Four", totalFee: 700000, amountPaid: 750000 }
];

// Run the report
displayReport(studentList);

/**
 * Justification:
 * - I used a **for loop** to go through each student and display results.
 * - I used **if...else conditions** in checkStatus() to determine fee status.
 * - I created **functions** (calculateBalance, checkStatus, displayReport)
 *   to keep the program organized and reusable.
 */
