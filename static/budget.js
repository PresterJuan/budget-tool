function adjustSpent(elem)
{
    line_item = document.getElementById(elem)
    new_expense = line_item.getElementsByClassName('new_expense')[0].textContent
    spent = line_item.getElementsByClassName('spent')[0].textContent
    console.log(new_expense)
    console.log(spent)
}