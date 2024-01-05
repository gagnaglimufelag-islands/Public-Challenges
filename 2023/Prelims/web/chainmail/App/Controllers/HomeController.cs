using System.Diagnostics;
using Microsoft.AspNetCore.Mvc;
using App.Models;
using App.Data;
using System.Text;
using Newtonsoft.Json;

namespace App.Controllers;

public class HomeController : Controller
{
    private readonly ILogger<HomeController> _logger;

    public HomeController(ILogger<HomeController> logger)
    {
        _logger = logger;
    }

    public IActionResult Index()
    {
        return View();
    }

    [HttpPost]
    async public Task<IActionResult> PostCodes()
    {
        Stream req = Request.Body;
        string json = await new StreamReader(req).ReadToEndAsync();

        PostcodeInput? inp = null;
        bool error = false;
        try
        {
            inp = JsonConvert.DeserializeObject<PostcodeInput>(json, new JsonSerializerSettings
            {
                TypeNameHandling = TypeNameHandling.Auto
            });
        }
        catch (Exception e)
        {
            _logger.LogTrace(e, "Error parsing JSON");
            error = true;
        }

        if (inp == null || error)
        {
            return base.Content("Invalid input", "text/plain", Encoding.UTF8);
        }

        string res = "Postcode does not exist";
        if (Postcode.Values.ContainsKey(inp.Postcode))
        {
            res = Postcode.Values[inp.Postcode];
        }
        return base.Content(res, "text/plain", Encoding.UTF8);
    }

    public IActionResult Privacy()
    {
        return View();
    }

    [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
    public IActionResult Error()
    {
        return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
    }
}
