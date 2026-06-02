from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from typing import Optional

#Every message in the vitalguard has this exact shape 
def error_response(status_code: int, message: str, details: Optional[list] = None):
    return JSONResponse(
        status_code=status_code,
        content={
            "ok": False,
            "message": message,
            "details": details or []
        }
    )


#Handler 1 - catches all raise HTTPExceptions(...)calls
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    return error_response(exc.status_code, exc.detail)


#Handler 2- catches all Pydantic validation failures(422)
async def validation_exception_handler(request: Request, exc:RequestValidationError):
    details=[
        {
            "field": "->".join(str(loc)for loc in err["loc"]),
            "message": err["msg"]

        }
        for err in exc.errors()
    ]

    return error_response(422, "Validation failed", details)

#Handler 3 - catches any unexpected crash(500)
async def generic_exception_handler(request: Request, exc:Exception):
    return error_response(500, "Something went wrong on our end")




    