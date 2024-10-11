
namespace ForumUnifeso.src.API.Controller.Auth
{
    using Microsoft.AspNetCore.Mvc;
    using ForumUnifeso.src.API.Service.Auth;
    using ForumUnifeso.src.API.Model.User;

    [ApiController]
    [Route("api/[controller]")]
    public class AuthController : ControllerBase
    {
        private readonly AuthService _authService;

        public AuthController(AuthService authService)
        {
            _authService = authService;
        }

        [HttpPost("login")]
        public IActionResult Login([FromBody] UserLogin login)
        {
            
            if (!ModelState.IsValid)
            {
                return BadRequest(ModelState); 
            }

            
            if (login.Username == "admin" && login.Password == "123")
            {
                var token = "Bearer " + _authService.GenerateJwtToken(login.Username);
                return Ok(new { token }); 
            }

            return Unauthorized(new { message = "Credenciais inválidas" });
        }
    }
}
