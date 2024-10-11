using AutoMapper;
using ForumUnifeso.src.API.Controller;
using ForumUnifeso.src.API.Interface;
using ForumUnifeso.src.API.Model;
using ForumUnifeso.src.API.View;
using FluentAssertions;
using Moq;
using Microsoft.AspNetCore.Mvc;

namespace UnitTests;

public class PostControllerTests
{
    private readonly Mock<IPostService> _postServiceMock;
    private readonly IMapper _mapper;
    private readonly PostController _controller;

    public PostControllerTests()
    {
        _postServiceMock = new Mock<IPostService>();

        var config = new MapperConfiguration(cfg =>
        {
            cfg.CreateMap<PostRequest, Post>()
    .ForMember(dest => dest.Author, opt => opt.MapFrom(src => new Person(1, src.Author.Name)));
            cfg.CreateMap<Post, PostResponse>();
            cfg.CreateMap<PersonRequest, Person>();
            cfg.CreateMap<Person, PersonResponse>();
        });
        _mapper = config.CreateMapper();

        _controller = new PostController(_postServiceMock.Object, _mapper);
    }

    [Fact]
    public async Task Test1Async()
    {
        // Arrange
        var postRequest = new PostRequest
        {
            Title = "Novo Post",
            Description = "Descrição do novo post",
            Date = DateTime.UtcNow,
            Author = new PersonRequest { Name = "Autor" }
        };

        var post = new Post(1, postRequest.Title, postRequest.Description, postRequest.Date, new Person { Name = postRequest.Author.Name });
        _postServiceMock.Setup(s => s.AddAsync(It.IsAny<Post>())).ReturnsAsync(post);

        // Act
        var result = await _controller.CreatePostAsync(postRequest);

        // Assert
        result.Should().BeOfType<CreatedAtActionResult>()
        .Which.Value.Should().BeOfType<PostResponse>()
        .Which.Title.Should().Be(postRequest.Title);
    }

    [Fact]
    public async Task CreatePostAsync_NullPostRequest_ReturnsBadRequest()
    {
        // Arrange
        PostRequest postRequest = null;

        // Act
        var result = await _controller.CreatePostAsync(postRequest);

        // Assert
        result.Should().BeOfType<BadRequestObjectResult>()
        .Which.Value.Should().Be("Post data is null.");
    }

    [Fact]
    public async Task CreatePostAsync_AutoMapperMappingException_ReturnsServerError()
    {
        // Arrange
        var postRequest = new PostRequest
        {
            Title = "Novo Post",
            Description = "Descrição do novo post",
            Date = DateTime.UtcNow,
            Author = new PersonRequest { Name = "Autor" }
        };

        _postServiceMock.Setup(s => s.AddAsync(It.IsAny<Post>()))
        .ThrowsAsync(new AutoMapperMappingException());

        // Act
        var result = await _controller.CreatePostAsync(postRequest);

        // Assert
        result.Should().BeOfType<ObjectResult>()
        .Which.StatusCode.Should().Be(500);
    }

    [Fact]
    public async Task CreatePostAsync_GeneralException_ReturnsServerError()
    {
        // Arrange
        var postRequest = new PostRequest
        {
            Title = "Novo Post",
            Description = "Descrição do novo post",
            Date = DateTime.UtcNow,
            Author = new PersonRequest { Name = "Autor" }
        };

        _postServiceMock.Setup(s => s.AddAsync(It.IsAny<Post>()))
        .ThrowsAsync(new Exception("Erro inesperado"));

        // Act
        var result = await _controller.CreatePostAsync(postRequest);

        // Assert
        result.Should().BeOfType<ObjectResult>()
        .Which.StatusCode.Should().Be(500);

        var objectResult = result as ObjectResult;
        objectResult?.Value.Should().Be("Erro inesperado");
    }
}