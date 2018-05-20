using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Bojo_Frontend.Entities;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;

namespace Bojo_Backend.Controllers
{
    [Route("api/[controller]")]
    public class TemperatureController : Controller
    {
        BojoContext _context;
        private const int DEFAULT_AMOUNT = 1000;
        public TemperatureController(BojoContext context)
        {
            _context = context;
        }

        // GET api/values
        [HttpGet]
        public async Task<ActionResult> Get()
        {
            return await Get(DEFAULT_AMOUNT);
        }

        // GET api/values/5
        [HttpGet("{amount}")]
        public async Task<ActionResult> Get([FromQuery]int amount)
        {
            var temperatures = _context.Temperatures.OrderByDescending(m => m.Time).Take(amount);
            var temperatureGroups = temperatures.GroupBy(t => t.Time); 
            var tempCollection = temperatureGroups.Select(tg => new TemperatureCollection(tg.AsQueryable()));
            return Ok(tempCollection);
        }
    }
}
