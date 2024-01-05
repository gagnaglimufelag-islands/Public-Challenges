using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using System.Linq.Dynamic.Core;

var builder = WebApplication.CreateBuilder(args);

var connectionString = builder.Configuration.GetConnectionString("DefaultConnection") ?? throw new InvalidOperationException("Connection string 'DefaultConnection' not found.");
builder.Services.AddDbContext<PostcodeDb>(options =>
    options.UseSqlite(connectionString)
);
builder.Services.AddDatabaseDeveloperPageExceptionFilter();
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerDocument(settings =>
{
    settings.Title = "postAPI";
    settings.Version = "1.33.7";
    settings.Description = "An awesome API to find Icelandic postcodes of towns and areas.";
});

var app = builder.Build();

app.MapGet("/", () => "Hello there!");
app.MapGet("/search", ([FromQuery] string? query, PostcodeDb db) => {
    if (query == null)
        query = "";
    return db.Postcodes.Where(String.Format("Hidden == false && (Name.Contains(\"{0}\"))", query)).ToList();
});

app.UseOpenApi();
app.UseSwaggerUi3();

app.Run();
