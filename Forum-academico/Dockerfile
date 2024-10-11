# Use a imagem base do .NET ASP.NET 8.0.8
FROM mcr.microsoft.com/dotnet/aspnet:8.0 AS base
WORKDIR /app
EXPOSE 80
EXPOSE 443

# Use a imagem do SDK do .NET 8.0.8 para build
FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build
WORKDIR /src

# Copie o arquivo de projeto e restaure dependências
COPY ["ForumUnifeso/ForumUnifeso.csproj", "ForumUnifeso/"]
RUN dotnet restore "ForumUnifeso/ForumUnifeso.csproj"

# Copie o restante do código e construa a aplicação
COPY . .
WORKDIR "/src/ForumUnifeso"
RUN dotnet build "ForumUnifeso.csproj" -c Release -o /app/build

# Publica a aplicação
FROM build AS publish
RUN dotnet publish "ForumUnifeso.csproj" -c Release -o /app/publish

# Use a imagem base para a etapa final
FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "ForumUnifeso.dll"]