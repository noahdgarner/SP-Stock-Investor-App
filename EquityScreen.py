one = {
    "operator": "AND",
    "clauses": [
        {
            "field":"marketcap",
            "operator" : "gt",
            "value" : "10000"
        },
        {
            "field":"industry_group",
            "operator":"eq",
            "value":"Electronic Equipment"
        },
        {
            "field" : "pricetoearnings",
            "operator" : "lt",
            "value" : "25"
        }
    ]
}

defensive = {
    "operator": "AND",
    "clauses": [
        {
            "field":"marketcap",
            "operator" : "gt",
            "value" : "750000000"
        },
        {
            "field" : "trailing_dividend_yield",
            "operator" : "gt",
            "value" : ".3"
        },
    ]
}



risky = {
    "operator": "AND",
    "clauses": [
        {
            "field": "marketcap",
            "operator": "gt",
            "value": "750000000"
        },
        {
            "field": "revenuegrowth",
            "operator": "gt",
            "value": ".25"
        },

    ]

}

risky2 = {
    "operator": "AND",
    "clauses": [
        {
            "field": "marketcap",
            "operator": "gt",
            "value": "750000000"
        },
        {
            "field": "five_yr_weekly_beta",
            "operator": "gt",
            "value": "1.3"
        },
        {
            "field": "revenuegrowth",
            "operator": "gt",
            "value": ".25"
        },

    ]

}