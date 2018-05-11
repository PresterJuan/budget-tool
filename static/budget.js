function adjustSpent(elem)
{
    line_item = document.getElementByID(elem)
    spent = line_item.getElementsByClassName('.spent')[0].textContent
    new_expense = line_item.getElementsByClassName('.new_expense')[0].textContent
    console.log(spent)
    console.log(new_expense)
}