"""
Vidhi AI
Document Processing Exceptions

Centralized exception hierarchy for the document processing pipeline.
"""

from __future__ import annotations


class DocumentProcessingError(Exception):
    """Base exception for document processing."""


class UploadError(DocumentProcessingError):
    """Raised when upload fails."""


class InvalidFileError(UploadError):
    """Raised when uploaded file is invalid."""


class UnsupportedFileTypeError(InvalidFileError):
    """Raised for unsupported file types."""


class FileTooLargeError(InvalidFileError):
    """Raised when file exceeds configured limit."""


class EmptyFileError(InvalidFileError):
    """Raised when uploaded file is empty."""


class DuplicateDocumentError(UploadError):
    """Raised when duplicate document is detected."""


class StorageError(DocumentProcessingError):
    """Raised when storage backend fails."""


class FileSaveError(StorageError):
    """Raised when file cannot be saved."""


class FileDeleteError(StorageError):
    """Raised when file cannot be deleted."""


class ParserError(DocumentProcessingError):
    """Base parser exception."""


class OCRProcessingError(ParserError):
    """Raised when OCR fails."""


class MetadataExtractionError(ParserError):
    """Raised when metadata extraction fails."""


class ClassificationError(DocumentProcessingError):
    """Raised when legal document classification fails."""


class ChunkingError(DocumentProcessingError):
    """Raised when document chunking fails."""


class EmbeddingGenerationError(DocumentProcessingError):
    """Raised when embedding generation fails."""


class VectorIndexError(DocumentProcessingError):
    """Raised when vector indexing fails."""


class SemanticSearchError(DocumentProcessingError):
    """Raised when semantic search fails."""


class ConfigurationError(DocumentProcessingError):
    """Raised for invalid document processing configuration."""
